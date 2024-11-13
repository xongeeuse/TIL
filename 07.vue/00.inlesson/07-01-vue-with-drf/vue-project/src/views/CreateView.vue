<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input v-model.trim="title" type="text" id="title" />
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" d="content"></textarea>
      </div>
      <input type="submit" />
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
const router = useRouter();

const title = ref("");
const content = ref("");

const createArticle = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
  })
    .then((res) => {
      console.log("게시글 작성 완!");
      router.push({
        name: "ArticleView",
      });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style></style>
