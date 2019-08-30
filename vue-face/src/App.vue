<template>
  <div id="app">
    <!--在当前区域进行跳转-->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  }
}
</script>
<style>
  *{
    margin: 0;
    padding: 0;
    list-style: none;
  }
  body{
    background-color: #f5f5f5;
  }
</style>
