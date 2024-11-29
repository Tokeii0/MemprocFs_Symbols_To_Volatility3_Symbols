# PDB to Volatility3 Symbols Converter

一个多线程批量转换工具，用于将 MemProcfs使用的 Windows PDB 文件转换为 Volatility3 符号文件（.json.xz）。

## 使用前提

1. 安装 Python 3.6+
2. 安装 Volatility3 框架
3. 准备好需要转换的 PDB 文件

## 目录结构

```
your_work_directory/
├── convert_pdbs_mt.py          # 本转换工具
├── volatility3/                # Volatility3 框架目录
├── Symbols_memprocfs/          # 源 PDB 文件目录
│   └── *.pdb                   # PDB 文件
└── Symbols_vol3/              # 输出目录（自动创建）
    └── *.pdb/                 # 对应的符号文件目录
        └── *.json.xz          # 转换后的符号文件
```

## 使用方法

1. 将脚本放在与 volatility3 目录同级的位置
2. 确保 Symbols_memprocfs 目录中包含需要转换的 PDB 文件
3. 运行脚本：
```bash
python convert_pdbs_mt.py
```

## 输出示例

转换后的文件将按照以下结构保存：
```
Symbols_vol3/
└── ntdll.pdb/
    └── 0ADF62812708CFE13125A0E82555162A-1.json.xz
```

## 自定义配置

如果需要调整线程数，可以修改脚本中的以下部分：
```python
max_workers = 20  # 设置为您想要的线程数
```

## 注意事项

1. 请确保有足够的磁盘空间存储转换后的文件
2. 转换过程可能较为耗时，取决于 PDB 文件的数量和大小
3. 建议在性能较好的机器上运行，以充分利用多线程优势

## 错误处理

- 脚本会自动捕获并显示处理过程中的错误
- 单个文件的处理失败不会影响其他文件的转换
- 最终会显示成功和失败的统计信息

