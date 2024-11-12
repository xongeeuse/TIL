<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <div>
      <p>이름: {{ selected.name }}</p>
      <p>잔고: {{ selected.balance }}</p>
      <button @click="addBalance">+</button>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { useBalanceStore } from "@/stores/balance";
const route = useRoute();
const store = useBalanceStore();
const selected = store.selectedBalance(route.params.name);
// console.log(store.selectedBalance(route.params.name));
// console.log(selected.value);
// console.log(route.params.name);

const addBalance = function () {
  selected.balance += 1000;
};
</script>

<style scoped></style>
