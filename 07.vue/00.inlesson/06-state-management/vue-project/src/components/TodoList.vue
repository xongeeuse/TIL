<template>
  <div>
    <h1>TodoList</h1>
    <TodoListItem v-for="todo in store.todos" :key="todo.id" :todo="todo" />
  </div>
</template>

<script setup>
import TodoListItem from "@/components/TodoListItem.vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
// console.log(store.todos);
</script>

<style scoped></style>
