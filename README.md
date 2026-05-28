# motrol_rating
自动化获取motrol牌谱rating

## 使用说明
1. **安装依赖**:
   需要根据requirements.txt安装依赖
   https://github.com/adryfish/fingerprint-chromium/releases/download/142.0.7444.175/ungoogled-chromium_142.0.7444.175-1.1_windows_x64.zip
   网址下载压缩包，文件夹重命名为fingerprint_browser
   任务队列需要redis，通过redis进行获取返回的结果ID，再根据ID进行查询数据内容，默认本地redis，详情配置在othertool.conredis文件
   默认是无头浏览器，开启俩个获取有效的token就行，因为接口有限制，开多个也能获取，但是要实现多代理IP去请求接口，不然也是返回限制无法获取
2. **启动后台服务**:
   ```bash
   python chrome_get_token.py
   ```
3. **运行主任务**:
   ```bash
   python get_user_rating.py
   ```
   
