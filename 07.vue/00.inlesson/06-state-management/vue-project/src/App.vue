<template>
  <div>
    <h1>Todo Project</h1>
    <h4>완료된 Todo 개수 : {{ store.doneTodosCount }}</h4>
    <TodoList />
    <TodoForm />
  </div>
</template>

<script setup>
import TodoForm from "@/components/TodoForm.vue";
import TodoList from "@/components/TodoList.vue";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
</script>

<style scoped></style>
