<template>
  <div class="child-box">
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ myProp.name }}</p>
    <p>나이: {{ myProp.age }}</p>
    <p>용돈: {{ myProp.balance }}</p>
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>
const props = defineProps({
  myProp: Object,
});

const emit = defineEmits(["updateBalance"]);

const giveMeAllowance = function () {
  emit("updateBalance", props.myProp.name);
};
</script>
<style scoped>
.child-box {
  border: 1px solid black;
  margin: 5px;
  padding: 5px;
}
</style>
