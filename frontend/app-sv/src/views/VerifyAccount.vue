<template>
  <div class="min-h-screen flex items-center justify-center bg-sky-50">
    <form @submit.prevent="verify" class="bg-white p-8 rounded shadow-md shadow-gray-400/50 w-full max-w-md">
      <h1 class="text-2xl font-bold mb-4 text-center text-sky-600">Verificación de Cuenta</h1>
      <input 
        v-model="password" 
        placeholder="Crear contraseña"
        type="password"
        class="input focus:outline-none focus:ring-1 focus:ring-sky-400 focus:border-sky-400"
      />
      <input 
        v-model="repeat_password" 
        placeholder="Repetir contraseña"
        type="password"
        class="input focus:outline-none focus:ring-1 focus:ring-sky-400 focus:border-sky-400"
      />
      <button class="w-full bg-sky-500 text-white py-2 rounded mt-4 hover:bg-sky-700">Activar Cuenta</button>
      <p v-if="message" class="mt-2 text-green-700">{{ message }}</p>
      <p v-if="error" class="mt-2 text-red-700">{{ error }}</p>
    </form>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import api from '../services/api'

export default {
  setup() {
    const route = useRoute()
    const token = route.params.token || route.query.token

    const password = ref('')
    const repeat_password = ref('')
    const message = ref('')
    const error = ref('')

    const verify = async () => {
      error.value = ''
      message.value = ''

      if (password.value !== repeat_password.value) {
        error.value = 'Las contraseñas no coinciden'
        return
      }

      try {
        const res = await api.post('/contest/verify/', {
          token,
          password: password.value
        })
        message.value = res.data.message || 'Cuenta activada con éxito'
      } catch (err: any) {
        error.value = err.response?.data?.error || 'Error al verificar la cuenta'
      }
    }

    return { password, repeat_password, message, error, verify }
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