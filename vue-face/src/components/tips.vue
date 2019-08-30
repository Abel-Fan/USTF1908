<template>
    <div class="bg">
        <!-- 提示信息图片开始 -->
        <div class="img-box">
            <img src="../assets/yuying_03.png" alt="">
        </div>
        <!-- 提示信息图片结束 -->
        <!-- 提示文字开始 -->
        <div class="tips-text">
            <div class="first-line">
                请将音量调整到适中
            </div>
            <div class="second-line">
                并跟随语音提示以及视频完成动作
            </div>
        </div>
        <!-- 提示文字结束 -->
        <!-- 按钮开始 -->

        <div class="know-btn" @click="jump()">
            我知道了
        </div>
        <!-- 按钮结束 -->
    </div>
</template>
<script>
export default {
    mounted:function(){
        this.say("请将音量调整到适中,并跟随语音提示以及视频完成动作");
    },
    methods: {
        say:function(content){
            var speech = window.speechSynthesis;
            var speak = new SpeechSynthesisUtterance();
            speak.text = content;
            speech.speak(speak);
        },
        jump() {
            this.$router.push("/video")
        }
    }
}
</script>
<style>
    /* 背景图片结束 */
    /* 提示信息图片开始 */
    .img-box{
        width: 6.94rem;
        margin: 1.63rem auto 0;
    }
    .img-box img{
        width: 100%;
    }
    /* 提示信息图片结束 */
    /* 提示文字开始 */
    .tips-text{
        margin-top: 0.91rem;
        text-align: center;
        font-size: 0.22rem;
        color: rgba(0, 0, 0, 0.4);
        font-weight: bold;
        font-family: "黑体";
    }
    /* 提示文字结束 */
    /* 按钮开始 */
    .know-btn{
        width: 3.68rem;
        height: 0.7rem;
        background: linear-gradient(90deg,
        #ffab32 0%,
        #ffce37 100%),
        linear-gradient(
                #000000,
                #000000);
        border-radius: 0.35rem;
        box-shadow: 0px 10px 24px 0px
        rgba(254, 211, 62, 0.75);
        margin: 3.65rem auto 0;
        color: #fff;
        font-size: 0.24rem;
        text-align: center;
        line-height: 0.7rem;
        letter-spacing: 1px;
    }
</style>