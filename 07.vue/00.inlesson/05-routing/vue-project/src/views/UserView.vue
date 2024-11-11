<template>
  <div>
    <h1>UserView</h1>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>

    <p>{{ $route.params }}</p>
    <p>{{ $route.params.id }}번 유저 프로필 페이지</p>
    <p>{{ userId }}번 유저 프로필 페이지</p>
    <button @click="goHome">Go Home!</button>
    <button @click="routeUpdate">100번 유저 페이지로!</button>
    <hr />
    <RouterView />
    <hr />
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRoute, useRouter } from "vue-router";
import { onBeforeRouteLeave, onBeforeRouteUpdate } from "vue-router";
import { ref } from "vue";
const route = useRoute();
const userId = ref(route.params.id);
const router = useRouter();

const goHome = function () {
  // 페이지 이동 개념: 뒤로가기 가능
  // router.push({ name: "home" });
  // 페이지 바꾸기 개념: 뒤로가기 불가능, history stack에 새로운 항목 push X
  router.replace({ name: "home" });
};
onBeforeRouteLeave((to, from) => {
  const answer = window.confirm("정말 떠나실 건가요?");
  if (!answer) {
    console.log("안갈거야!");
    return false;
  }
});
const routeUpdate = function () {
  router.push({ name: "user", params: { id: 100 } });
};

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>

<style lang="scss" scoped></style>
