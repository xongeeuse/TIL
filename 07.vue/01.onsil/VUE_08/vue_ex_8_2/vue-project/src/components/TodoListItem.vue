<template>
  <!-- <div>
    <h3>TodoListItem</h3>
    <p>{{ todo }}</p>
    <hr />
  </div> -->
  <div v-if="todo">
    <h4>{{ todo.work }}</h4>
    <p>{{ todo.content }}</p>
    <p>{{ todo.is_completed }}</p>
    <p>{{ todo.created_at }}</p>
    <hr />
  </div>
</template>

<script setup>
defineProps({
  todo: Object,
});
</script>

<style scoped></style>
