<template>
  <div class="mt-3 ms-5 me-5">
    <div class="contact_2l row">
      <div class="col-md-12">
        <h4>글 작성하기</h4>
      </div>
    </div>

    <div class="contact_2l1 mt-3 row">
      <div class="col-md-6">
        <div class="contact_2l1i">
          <input
            class="form-control"
            placeholder="제목*"
            type="text"
            v-model="title"
          />
        </div>
      </div>
    </div>

    <div class="contact_2l1 mt-3 row">
      <div class="col-md-12">
        <div class="contact_2l1i">
          <textarea
            placeholder="내용을 입력하세요."
            class="form-control form_text"
            v-model="content"
          ></textarea>
          <h6 class="mt-3 mb-3">
            <button class="button" @click="submitArticle">Submit</button>
          </h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title: null,
      content: null,
    };
  },
  methods: {
    ...mapActions(['createArticle']),
    submitArticle() {
      this.createArticle({
        title: this.title,
        content: this.content,
      });
      this.$router.push({ name: 'community' });
    },
  },
};
</script>

<style></style>
