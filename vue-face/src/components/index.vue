<template>
    <div>
        <!--机器人-->
        <div class="box1">
            <div class="yuan">
                <div>
                    <img src="../assets/robot.png" class="biankuang">
                </div>
                <p class="title2">JION.AI.BOX</p>
            </div>
        </div>
        <div class="button1" v-on:click="handmove()">手动登录</div>
        <div class="button2" v-on:click="faceClick()">脸部识别</div>
    </div>
</template>
<script>
    export default {
        methods: {
            handmove: function () {
                this.$router.push("/startident")
            },
            faceClick: function () {
                this.$router.push("/tips1")
            }
        }
    }
</script>
<style scoped="scoped">
    .box1{
        width: 4.18rem;
        height: 4.18rem;
        background-color: #f5f5f5;
        margin: 0 auto;
        margin-top: 1.15rem;
        position: relative;
    }
    .yuan{
        width: 4.12rem;
        height: 4.12rem;
        background-color: #eef2f1;
        border-radius: 50%;
        position: absolute;
        left: 0.1rem;
        top: 0.1rem;
    }
    .biankuang{
        width: 3.58rem;
        height: 3.58rem;
        border-radius: 50%;
        position: absolute;
        left: 0.28rem;
        top: 0.28rem;
    }
    .title2{
        font-size: 0.4rem;
        color: rgba(0,0,0,0.45);
        text-align: center;
        line-height: 0.4rem;
        margin-top: 5rem;
    }
    .button1{
        width: 3.7rem;
        height: 0.7rem;
        border-radius: 0.5rem;
        font-size: 0.24rem;
        color: #fff;
        text-align: center;
        line-height: 0.7rem;
        box-shadow:0px 4px 15px #3ab7ff;/*阴影*/
        background: linear-gradient(to right, #3e9dff , #41c3ff);
        margin-left: 27%;
        margin-top: 60%;
    }
    .button2{
        width: 3.7rem;
        height: 0.7rem;
        border-radius: 0.5rem;
        font-size: 0.24rem;
        color: #fff;
        text-align: center;
        line-height: 0.7rem;
        box-shadow:0px 4px 15px #3ab7ff;/*阴影*/
        background: linear-gradient(to right,#33cf7c, #5eed5f);
        margin-left: 27%;
        margin-top: 10%;
    }
</style>