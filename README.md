# cobweb 蛛网 - 图型化显示子域名和解析IP对应关系

# 效果图

网状显示关系可拖动

![](img/cobweb1.jpg)

可手动筛选单独高亮显示

![](img/cobweb2.jpg)

# 使用依赖

> 仅限linux下使用

> python3 [sudo pip3 install pyvis]

# 使用方法

1. 安装`dnsx`

```
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

2. 运行`dnsx`，获取子域名`collect_subdomains.txt`解析结果`active_subdomains2ips.txt`

```
dnsx -l collect_subdomains.txt -silent -a -resp | sed 's/\[//g' | sed 's/\]//g' | tee active_subdomains/active_subdomains2ips.txt
```

3. 运行`Generate_yaml.sh`，得到`active_subdomains/active_subdomains2ips.yaml`

```
bash Generate_yaml.sh
```

4. 运行cobweb.py，浏览器会自动打开

```
sudo python3 cobweb.py --domain tesla.com --file active_subdomains/subdomains2ips.yaml
```

# 感谢

https://github.com/screetsec/Sudomy
