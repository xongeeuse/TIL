<template>
  <div>
    <h1>ArticleView</h1>
    <RouterLink :to="{ name: 'CreateView' }">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
import ArticleList from "@/components/ArticleList.vue";
import { useCounterStore } from "@/stores/counter";
import { onMounted } from "vue";

const store = useCounterStore();

onMounted(() => {
  // mount 되기 전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getArticles();
});
</script>

<style></style>
