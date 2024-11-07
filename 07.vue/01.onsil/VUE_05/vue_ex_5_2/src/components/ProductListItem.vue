<template>
  <div>
    <span> {{ product.name }} - {{ product.price }}원 </span>
    <button>장바구니에 추가</button>
  </div>
</template>

<script setup>
defineProps({
  product: Object,
});
</script>

<style scoped></style>
