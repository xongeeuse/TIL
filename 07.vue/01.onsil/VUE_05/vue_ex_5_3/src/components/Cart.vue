<template>
  <div>
    <h1>장바구니</h1>
    <li v-for="item in cart" :key="item.id">
      {{ item.name }} - {{ item.price }}원
      <span v-if="item.quantity > 1">* {{ item.quantity }}개</span>
      <button @click="deleteItem(item)">삭제</button>
    </li>
  </div>
</template>

<script setup>
const props = defineProps({
  cart: Array,
});
const emit = defineEmits(["deleteItem"]);
const deleteItem = function (item) {
  emit("deleteItem", item);
};
</script>

<style scoped></style>
