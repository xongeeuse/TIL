<template>
  <div>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="goToUpdate(balance.name)" class="btn btn-primary">
      updateBalance
    </button>

    <hr />
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
defineProps({
  balance: Object,
});

const goToUpdate = function (name) {
  router.push({ name: "update", params: { name: name } });
};
</script>

<style scoped></style>
