import os
import glob
from concurrent.futures import ThreadPoolExecutor
import subprocess
from pathlib import Path
import threading

# 用于打印的锁
print_lock = threading.Lock()

def safe_print(message):
    """线程安全的打印函数"""
    with print_lock:
        print(message)

def convert_pdb(pdb_path):
    """转换单个PDB文件"""
    try:
        # 获取pdbconv.py的完整路径
        script_path = os.path.join(os.getcwd(), "volatility3", "framework", "symbols", "windows", "pdbconv.py")
        
        # 构建命令
        cmd = ["python", script_path, "-f", pdb_path]
        
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            safe_print(f"成功处理: {pdb_path}")
            return True
        else:
            safe_print(f"处理失败: {pdb_path}")
            safe_print(f"错误信息: {result.stderr}")
            return False
            
    except Exception as e:
        safe_print(f"处理出错: {pdb_path}")
        safe_print(f"错误信息: {str(e)}")
        return False

def main():
    # 设置工作目录为脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 获取所有PDB文件
    pdb_files = []
    symbols_memprocfs = Path("Symbols_memprocfs")
    
    # 递归查找所有.pdb文件
    for pdb_file in symbols_memprocfs.rglob("*.pdb"):
        if pdb_file.is_file():
            pdb_files.append(str(pdb_file))
    
    total_files = len(pdb_files)
    safe_print(f"找到 {total_files} 个PDB文件待处理")
    
    # 获取CPU核心数，用作线程数
    max_workers = os.cpu_count()
    if max_workers is None:
        max_workers = 20
    
    # 创建线程池
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        futures = [executor.submit(convert_pdb, pdb_file) for pdb_file in pdb_files]
        
        # 统计成功和失败的数量
        success_count = sum(1 for future in futures if future.result())
        
    # 打印最终统计信息
    safe_print("\n处理完成!")
    safe_print(f"总文件数: {total_files}")
    safe_print(f"成功处理: {success_count}")
    safe_print(f"失败数量: {total_files - success_count}")

if __name__ == "__main__":
    main()
