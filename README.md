<p align='center'>
    <img style='width:400px' src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Dapr_logo.svg/1200px-Dapr_logo.svg.png"/>
</p>

# Introduction
## Dapr(Distributed Application Runtime)   
他是由微軟發展出來，純 Open Source 的專案，專門用來處理開發Microservice 時，所遇到的一些問題。   
且他支援任何語言，任何平台，透過 http/gRPC 來調用中間 Dapr 的服務。   
所以你可以想像，你想要執行的服務，只需要透過 http/gRPC 的調用，就可以使用。   
(簡單來說就是 call service 當成一個 function call的概念)
<img src="https://docs.dapr.io/images/service-invocation-overview.png"/>
整體可分為以下方法:
<img src="https://docs.dapr.io/images/building_blocks.png"/>

<br/>  


# How to Build
## Environment
- python 3.9.13
- Ubuntu 20.04

## Installtion
```
python -m pip install dapr-ext-fastapi
```
## Component Config
- default Schema
詳細使用方式可參閱 [官方文檔](https://docs.dapr.io/operations/components/component-schema/)
```
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: [COMPONENT-NAME]
  namespace: [COMPONENT-NAMESPACE]
spec:
  type: [COMPONENT-TYPE]
  version: v1
  initTimeout: [TIMEOUT-DURATION]
  ignoreErrors: [BOOLEAN]
  metadata:
  - name: [METADATA-NAME]
    value: [METADATA-VALUE]
```
## Deploy
- Sample  
詳細參閱 [部屬範例](./docker/)

<br/>

# How to use
- Invoke_method  
可觸發app中的api，並返回response
- pub/sub  
可設定subscibe & publish，當publish推送訊息時，可根據設定之pubsub和topic觸發相對應之subscibe方法
- Sample  
詳細參閱 [使用範例](./sample/)

---
## 資料來源
[Dapr官方文件](https://docs.dapr.io/)