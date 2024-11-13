<template>
  <main>
    <h1>할 일 목록</h1>
    {{ store.todos }}
  </main>
</template>

<script setup>
import { onMounted } from "vue";
import { useTodoStore } from "@/stores/todoStore";
const store = useTodoStore();

onMounted(() => {
  store.getTodos();
});
</script>

<style></style>
