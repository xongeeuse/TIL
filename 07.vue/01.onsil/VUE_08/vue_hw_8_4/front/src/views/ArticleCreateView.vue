<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 :</label>
        <input v-model.trim="title" type="text" id="title" />
      </div>
      <div>
        <label for="content">내용 :</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="create" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
const router = useRouter();
const title = ref(null);
const content = ref(null);

const createArticle = function () {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/api/v1/articles/",
    data: {
      title: title.value,
      content: content.value,
    },
  })
    .then((res) => {
      router.push({
        name: "home",
      });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
