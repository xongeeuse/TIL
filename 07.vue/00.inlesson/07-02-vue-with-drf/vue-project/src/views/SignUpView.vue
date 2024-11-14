<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input v-model.trim="username" type="text" id="username" /><br />

      <label for="password1">password : </label>
      <input v-model.trim="password1" type="password" id="password1" /><br />

      <label for="password2">password confirmation : </label>
      <input v-model.trim="password2" type="password" id="password2" />

      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
</script>

<style></style>
