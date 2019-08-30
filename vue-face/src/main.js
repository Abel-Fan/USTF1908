import Vue from 'vue'
import App from './App.vue'
// 引入路由
import routers from "./router/index.js"

Vue.config.productionTip = false

new Vue({
  router: routers,
  render: h => h(App),
}).$mount('#app')
