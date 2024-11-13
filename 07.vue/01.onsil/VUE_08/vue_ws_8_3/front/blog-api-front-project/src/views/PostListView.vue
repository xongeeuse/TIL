<template>
  <div>
    <h1>게시글 목록 페이지</h1>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { usePostStore } from "@/stores/counter";
const store = usePostStore();
onMounted(() => {
  store.getPosts();
});
</script>

<style scoped></style>
