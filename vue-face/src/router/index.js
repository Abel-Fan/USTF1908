/*
* @author GuoXianglian
* @date 2019-08-21
*/
// 引入vue模块
import Vue from "vue";
// 引入vue-router插件
import vueRouter from "vue-router";
// 使用vue-router插件
Vue.use(vueRouter);

import Index from "@/components/index.vue";
import startident from "@/components/startident.vue";
import confirmident from "@/components/confirmident.vue";
import tips from "@/components/tips.vue";
import tips1 from "@/components/tips1.vue";
import video from "@/components/video.vue";
import shibiezhong from "@/components/shibiezhong.vue";

export default new vueRouter({
    routes: [
        {
            path: "/", // 路径
            name: "index", // 名字
            component: Index
        },
        {
            path: "/startident", // 路径
            name: "startident", // 名字
            component: startident
        },
        {
            path: "/confirmident", // 路径
            name: "confirmident", // 名字
            component: confirmident
        },
        {
            path: "/tips", // 路径
            name: "tips", // 名字
            component: tips
        },
        {
            path: "/tips1", // 路径
            name: "tips1", // 名字
            component: tips1
        },
        {
            path: "/video", // 路径
            name: "video", // 名字
            component: video
        },
        {
            path: "/shibiezhong", // 路径
            name: "shibiezhong", // 名字
            component: shibiezhong
        }
    ]
})



