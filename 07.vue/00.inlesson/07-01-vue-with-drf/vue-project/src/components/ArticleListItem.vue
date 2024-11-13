<template>
  <div>
    <h4>{{ article.id }}</h4>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }"
      >Detail</RouterLink
    >

    <hr />
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
defineProps({
  article: Object,
});
</script>
