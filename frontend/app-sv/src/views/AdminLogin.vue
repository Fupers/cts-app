<template>
  <div class="min-h-screen flex items-center justify-center bg-sky-50">
    <form @submit.prevent="login" class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h1 class="text-2xl font-bold mb-4 text-center text-sky-600">Login Administrador</h1>
      <input 
        v-model="username" 
        placeholder="Usuario"
        type="name"
        class="input"
      />
      <input 
        v-model="password" 
        placeholder="Contraseña"
        type="password"
        class="input"
      />
      <button class="w-full bg-sky-500 text-white py-2 rounded mt-4 hover:bg-sky-700">Ingresar</button>
      <p v-if="errorMessage" class="mt-2 text-red-600 text-sm">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script lang="ts">
import api from '../services/api'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const username = ref('')
    const password = ref('')
    const errorMessage = ref('')
    const router = useRouter()

    const login = async () => {
      errorMessage.value = ''
      try {
        const res = await api.post("/admin/login/", {
          username: username.value, // ahora usamos username
          password: password.value,
        });
        localStorage.setItem("adminToken", res.data.access);
        router.push("/admin/contestants");
      } catch (err: any) {
        errorMessage.value = err.response?.data?.detail || "Error al iniciar sesión"
      }
    };

    return { username, password, login, errorMessage }
  }
}
</script>

<style scoped>
.input {
  display: block;
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 0.75rem;
  border: 1px solid #adadadff;
  border-radius: 0.375rem;
}
</style>
