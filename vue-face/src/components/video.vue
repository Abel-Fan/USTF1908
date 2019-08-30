<template>
    <div class="bg">
        <!-- 相框开始 -->
        <div class="album">
            <video src="" autoplay class="video">
                <canvas width="202" height="256" id="canvas"></canvas>
            </video>
        </div>
        <!-- 相框结束 -->
        <!-- 提示语开始 -->
        <div class="tips-text">
            请正脸对准屏幕
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
            this.getVideo();
        },
        methods: {
            getVideo: function () {
                var video = document.querySelector(".video");
                var canvas = document.querySelector("#canvas");
                var videox = {
                    video: {
                        width: 202,
                        height: 256
                    }
                };
                var promise = navigator.mediaDevices.getUserMedia(videox);
                let that = this
                promise.then((data) => {
                    video.srcObject = data;
                    // 视频执行时获取base64图片
                    let flag = true
                    video.onprogress = function () {
                        if(!flag){
                            return
                        }
                        flag = false
                        var cans = canvas.getContext("2d");
                        cans.drawImage(video, 0, 0);
                        // 转换成base64编码图片
                        var baseimg = canvas.toDataURL("image/jpeg").substr(23)
                        fetch("/photo",{
                          method:"post",
                          headers: {
                            'content-type': 'application/x-www-form-urlencoded'
                          },
                          body:"url="+baseimg+"&name="+localStorage.name
                        }).then((r)=>{
                          return r.json()
                        }).then((data)=>{
                          if(data['error_msg']){
                              flag = true
                          }else{
                              that.$router.push("/")
                          }
                        })

                    }


                })
            }
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