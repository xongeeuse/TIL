<template>
  <div>
    <RouterLink :to="{ name: 'create' }">
      <button>게시글 생성</button>
    </RouterLink>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/articles";
import ArticleListItem from "@/components/ArticleListItem.vue";
const store = useArticleStore();
onMounted(() => {
  store.getArticles();
});
</script>

<style lang="scss" scoped></style>
