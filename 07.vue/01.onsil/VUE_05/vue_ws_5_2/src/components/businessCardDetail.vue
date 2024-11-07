<template>
  <div class="card">
    <h4>이름: {{ card.name }}</h4>
    <p>직함: {{ card.title }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  card: Object,
});
</script>

<style scoped>
.card {
  /* border: 1px solid gray; */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  background-color: lightgray;
  margin: 10px;
  width: 300px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
