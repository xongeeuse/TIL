<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage
      v-for="balance in store.balances"
      :key="balance.name"
      :balance="balance"
    />
  </div>
</template>

<script setup>
import { useBalanceStore } from "@/stores/balance";
import MainPage from "@/components/MainPage.vue";
const store = useBalanceStore();
</script>

<style scoped></style>
