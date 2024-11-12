<template>
  <div class="child-box">
    <h2>자식 컴포넌트</h2>
    {{ child.name }}
  </div>
</template>

<script setup>
defineProps({
  child: Object,
});
</script>

<style scoped>
.child-box {
  background-color: white;
  border: 1px solid black;
  margin: 10px;
  padding: 10px;
}
</style>
