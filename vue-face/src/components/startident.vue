<template>
    <div class="box">
        <!--  人头像-->
        <div class="one"></div>
        <div class="two"></div>
        <div class="three">
            <img src="../assets/person.png" class="person">
        </div>
        <div class="title">请通过人脸识别验证您的身份</div>
        <p class="title1">请按照以下步骤完成脸部验证</p>
        <div class="shuru">
            <div class="yuandian"></div>
            <div class="text">
                <input type="wenzi" placeholder="请输入您的名字" style="width:3rem" v-model="name">
            </div>
            <div class="close">+</div>
        </div>
        <div class="button" v-on:click="submit()">开始识别</div>
    </div>
</template>
<script>
    var speech = window.speechSynthesis;
    export default {
        data: function () {
          return {
              name: ""
          }
        },
        mounted:function(){
            this.say("请通过人脸识别验证您的身份,请按照以下步骤完成脸部验证");
        },
        methods: {
            say:function(content){
                var speak = new SpeechSynthesisUtterance();
                speak.text = content;
                speech.speak(speak);
            },
            submit: function () {
                if(this.name == "") {
                    speech.cancel();
                    this.say("请输入您的姓名");
                } else {
                    speech.cancel();
                    localStorage.name = this.name
                    this.$router.push("/confirmident")
                }
            }
        }
    }
</script>
<style scoped>
    .box{
        width: 4.18rem;
        height: 4.18rem;
        background-color: #f5f5f5;
        margin: 0 auto;
        margin-top: 1.15rem;
        position: relative;
    }
    .one{
        width: 4.12rem;
        height: 4.12rem;
        background-color: #eef2f1;
        border-radius: 50%;
    }
    .two{
        width: 3.19rem;
        height: 3.19rem;
        background-color: #deefe6;
        border-radius: 50%;
        position: absolute;
        left: 0.51rem;
        top: 0.51rem;
    }
    .three{
        width: 2.17rem;
        height: 2.17rem;
        background-color: #cbe9dc;
        border-radius: 50%;
        position: absolute;
        left: 1rem;
        top: 1rem;
    }
    .person{
        width: 1.6rem;
        height: 1.7rem;
        margin-top: 0.17rem;
        margin-left: 0.28rem;
    }
    .title{
        font-size: 0.28rem;
        color: #2bd86f;
        text-align: center;/*文本居中*/
    }
    .title1{
        font-size: 0.22rem;
        color: rgba(0,0,0,0.45);
        text-align: center;
        line-height: 0.4rem;
    }
    .shuru{
        width: 100%;
        height: 0.75rem;
        border-bottom-color: #dbdbdb;
        border-bottom-width: 1px;
        border-bottom-style: solid;
        margin: 0 auto;
    }
    .yuandian{
        width: 0.18rem;
        height: 0.09rem;
        background-color: #ff6600;
        float: left;
        border-radius: 0.05rem;
        margin-top: 0.55rem;
        margin-right: 0.23rem;
        box-shadow:0px 4px 15px #ffcb2e;

    }
    .text{
        position: absolute;
        left: 0.5rem;
        color: rgba(0,0,0,0.45);
        font-size: 0.22rem;
        line-height: 0.57rem;
        margin-top: 0.27rem;
    }
    .close{
        float: right;
        font-size: 0.24rem;
        color: rgba(0.0.0.0.45);
        line-height: 0.57rem;
        transform: rotate(45deg);
        margin-top: 0.30rem;
    }
    .wenzi{
        width: 3rem;
        height: 100%;
        border: 0;
        background-color: #f4f4f4;
    }
    .button{
        width: 3.7rem;
        height: 0.7rem;
        border-radius: 0.5rem;
        font-size: 0.24rem;
        color: #fff;
        text-align: center;
        line-height: 0.7rem;
        box-shadow:0px 4px 15px #3ab7ff;/*阴影*/
        background: linear-gradient(to right, #3e9dff , #41c3ff);
        margin: 0 auto;
        margin-top: 30%;
    }

    .buttongray{
        width: 3.7rem;
        height: 0.7rem;
        border-radius: 0.5rem;
        font-size: 0.24rem;
        color: #333;
        text-align: center;
        line-height: 0.7rem;
        background: #cfcfcf;
        margin: 0 auto;
        margin-top: 30%;
    }
</style>