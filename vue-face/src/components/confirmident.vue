<template>
    <div >
        <!--第三章-->
        <div class="box2">
            <img src="../assets/2_03.png" class="shibie">
            <div class="button3" v-on:click="confirmFun()">确认</div>
            <div class="button4" v-on:click="resetFun()">取消</div>
        </div>
    </div>
</template>
<script>
    export default {
        methods: {
            confirmFun: function() {
                this.$router.push("/tips")
            },
            resetFun: function () {
                this.$router.push("/startident")
            }
        }
    }
</script>
<style scoped>
    .box2{
        width: 4.72rem;
        height: 3.20rem;
        border-radius: 10%;
        position: relative;
        margin-left: 20%;
        margin-top: 40%;
    }
    .shibie{
        width: 4.72rem;
        height: 3.20rem;
        border-radius: 10%;
        box-shadow:0px 4px 15px #c5c5c6;
        position: absolute;
        top: 0;
    }
    .button3{
        width: 1rem;
        height: 0.4rem;
        border-radius: 0.5rem;
        font-size: 0.22rem;
        color: #fff;
        text-align: center;
        line-height: 0.4rem;
        box-shadow:0px 4px 15px #3ab7ff;/*阴影*/
        background: linear-gradient(to right,#33cf7c, #5eed5f);
        position: absolute;
        top: 65%;
        left: 20%;
    }
    .button4{
        width: 1rem;
        height: 0.4rem;
        border-radius: 0.5rem;
        font-size: 0.22rem;
        color: #a5eabb;
        text-align: center;
        line-height: 0.4rem;
        background-color: #eafcf0;
        position: absolute;
        top: 65%;
        left: 60%;
    }
</style>