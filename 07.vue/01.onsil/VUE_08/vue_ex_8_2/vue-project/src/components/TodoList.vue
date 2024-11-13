<template>
  <div>
    <!-- <h1>TodoList</h1> -->
    <TodoListItem v-for="todo in todos" :key="todo.id" :todo="todo" />
  </div>
</template>

<script setup>
import TodoListItem from "@/components/TodoListItem.vue";
defineProps({
  todos: Array,
});
</script>

<style scoped></style>
