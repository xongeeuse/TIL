<template>
  <div class="child-box">
    <h3>자식 페이지입니다.</h3>
    <p>{{ myProp.name }}</p>
    <p>{{ myProp.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  myProp: Object,
});
</script>

<style scoped>
.child-box {
  border: 1px solid black;
  margin: 5px;
}
</style>
