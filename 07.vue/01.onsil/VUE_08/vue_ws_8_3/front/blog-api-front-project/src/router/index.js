import MainView from "@/views/MainView.vue";
import PostListView from "@/views/PostListView.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "main",
      component: MainView,
    },
    {
      path: "/posts",
      name: "postlist",
      component: PostListView,
    },
  ],
});

export default router;
