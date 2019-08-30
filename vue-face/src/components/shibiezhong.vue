<template>
    <div class="bg">
        <!-- 相框开始 -->
        <div class="album">
            <canvas></canvas>
            <video src="" width="202" height="256" autoplay></video>
        </div>
        <!-- 相框结束 -->
        <!-- 提示语开始 -->
        <div class="tips-text">
            <ul class="dots">
                <li class="dot d"></li>
                <li class="dot c"></li>
                <li class="dot b"></li>
                <li class="dot a"></li>
                <li class="dot b"></li>
                <li class="dot c"></li>
                <li class="dot d"></li>
            </ul>
            识别中，请不要着急
        </div>
        <!-- 提示语结束 -->
        <!-- 公司名称开始 -->
        <div class="company">
            UEK TECHNOLOGY
        </div>
        <!-- 公司名称结束 -->
    </div>
</template>

<script>
    export default {
        mounted() {
            navigator.mediaDevices.getUserMedia({
                video:{
                    width:202,
                    height:256
                }
            }).then((data)=>{
                var video = document.querySelector("video");
                var canvas = document.querySelector("canvas");
                video.srcObject = data;
                let flag = true
                let num = 0
                video.onprogress = ()=>{
                    if(!flag){
                      return
                    }
                    flag = false

                    var can = canvas.getContext("2d");
                    can.drawImage(video, 0, 0);
                    var data = canvas.toDataURL("image/jpeg", .7).substr(23);
                    var name = localStorage.username;

                    fetch("/check",{
                      method:"post",
                      headers: {
                        'content-type': 'application/x-www-form-urlencoded'
                      },
                      body:"url="+data+"&name="+name
                    }).then((r)=>{
                      return r.json()
                    }).then((data)=>{

                      if(data['error_code']){
                        flag = true
                      }else{
                        flag=false
                          if(data['result'][0]['scores'][0]>90){
                              console.log(data)
                              alert("检测成功")
                          }else{
                              num+=1
                              flag = true
                              if(num>=5){
                                  flag = false
                                  alert("检测失败")
                              }
                          }
                      }
                    })


                }
            })

        }
    }
</script>

<style scoped>
    /* 头像开始 */
    .album{
        width: 3.95rem;
        height: 5.1rem;
        border: 1px solid rgba(0, 0, 0, 0.2);
        position: absolute;
        top: 2.26rem;
        left: calc(50% - 1.975rem);
    }
    .album canvas{
        width: 100%;
        height: 100%;
        position: absolute;
        left: 0;
        top: 0;
    }
    .album video{
        width: 100%;
        height: 100%;
        position: absolute;
        left: 0;
        top: 0;
    }
    /* 头像结束 */
    /* 提示语开始 */
    .tips-text{
        width: 100%;
        text-align: center;
        color: #a0a0a0;
        font-size: 0.26rem;
        position: absolute;
        bottom: 2.08rem;
    }
    /* 提示语结束 */
    /* 公司名称开始 */
    .company{
        width: 100%;
        text-align: center;
        color: #dadada;
        font-size: 0.16rem;
        position: absolute;
        bottom: 0.55rem;
    }
    /* 公司名称结束 */
    .dots{
        width: 1.72rem;
        height: 0.18rem;
        display: flex;
        justify-content: space-between;
        margin: 0 auto 0.2rem;
    }
    .dots .dot{
        width: 0.18rem;
        height: 0.18rem;
        border-radius: 50%;
    }
    .dot.a{
        background: #2dc27a;
    }
    .dot.b{
        background: #2dc27a;
        opacity: 0.5;
    }
    .dot.c{
        background: #2dc27a;
        opacity: 0.3;
    }
    .dot.d{
        background: #2dc27a;
        opacity: 0.1;
    }

</style>
