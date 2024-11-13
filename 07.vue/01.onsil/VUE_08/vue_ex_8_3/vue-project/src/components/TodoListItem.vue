<template>
  <div>
    <p>{{ todo.work }}</p>
    <p>{{ todo.content }}</p>
    <p>{{ todo.is_completed }}</p>
    <p>{{ todo.created_at }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: todo.id } }">
      <button>상세보기</button>
    </RouterLink>
  </div>
  <hr />
</template>

<script setup>
import { RouterLink } from "vue-router";
import { defineProps } from "vue";
defineProps({
  todo: Object,
});
</script>
