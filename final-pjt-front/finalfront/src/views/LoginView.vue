<template>
  <div class="blog_1r1 p-4 mt-4 w-50" style="margin: 0 auto">
    <h4>Login <span class="col_red">Form</span></h4>
    <hr class="mb-4" />
    <div class="input-group input-group-merge">
      <div
        class="input-group-text bg-transparent text-white border-right-0"
        data-password="false"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-person"
          viewBox="0 0 16 16"
        >
          <path
            d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"
          />
        </svg>
      </div>
      <input
        type="username"
        id="username"
        class="form-control bg-transparent"
        placeholder="Username"
        v-model="userInfo.username"
      />
    </div>
    <div class="input-group input-group-merge mt-3">
      <div
        class="input-group-text bg-transparent text-white border-right-0"
        data-password="false"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-key"
          viewBox="0 0 16 16"
        >
          <path
            d="M0 8a4 4 0 0 1 7.465-2H14a.5.5 0 0 1 .354.146l1.5 1.5a.5.5 0 0 1 0 .708l-1.5 1.5a.5.5 0 0 1-.708 0L13 9.207l-.646.647a.5.5 0 0 1-.708 0L11 9.207l-.646.647a.5.5 0 0 1-.708 0L9 9.207l-.646.647A.5.5 0 0 1 8 10h-.535A4 4 0 0 1 0 8zm4-3a3 3 0 1 0 2.712 4.285A.5.5 0 0 1 7.163 9h.63l.853-.854a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.793-.793-1-1h-6.63a.5.5 0 0 1-.451-.285A3 3 0 0 0 4 5z"
          />
          <path d="M4 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
        </svg>
      </div>
      <input
        type="password"
        id="password"
        class="form-control bg-transparent"
        placeholder="password"
        v-model="userInfo.password"
        @keyup.enter="fetchLogin(userInfo)"
      />
    </div>

    <h6 class="mt-3">
      <button class="button border-0" @click="fetchLogin(userInfo)">
        Login
      </button>
    </h6>
    <h6 class="mt-3">
      <router-link :to="{ name: 'signup' }" class="col_red"
        >계정이 없으신가요? 계정 만들러 가기</router-link
      >
    </h6>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'LoginView',
  data() {
    return {
      userInfo: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    ...mapActions(['fetchLogin']),
  },
};
</script>

<style></style>
