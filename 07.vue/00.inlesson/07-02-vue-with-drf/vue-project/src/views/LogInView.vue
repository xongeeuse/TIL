<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input v-model.trim="username" type="text" id="username" /><br />

      <label for="password">password : </label>
      <input v-model.trim="password" type="password" id="password" /><br />

      <input type="submit" value="logIn" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();

const username = ref(null);
const password = ref(null);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style></style>
