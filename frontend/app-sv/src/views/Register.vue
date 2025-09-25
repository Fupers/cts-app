<template>
  <div class="min-h-screen flex items-center justify-center bg-sky-50">
    <form @submit.prevent="register" class="bg-white p-8 rounded shadow-md shadow-gray-400/50 w-full max-w-md">
      <h1 class="text-2xl font-bold mb-4 text-center text-sky-600">Registro Concurso</h1>
      <input 
        v-model="name" 
        placeholder="Nombre completo"
        type="text"
        class="input focus:outline-none focus:ring-1 focus:ring-sky-400 focus:border-sky-400"
      />
      <input 
        v-model="email" 
        placeholder="Correo electrónico" 
        type="email" 
        class="input focus:outline-none focus:ring-1 focus:ring-sky-400 focus:border-sky-400"
      />
      <input 
        v-model="phone" 
        placeholder="Teléfono" 
        type="tel"
        class="input focus:outline-none focus:ring-1 focus:ring-sky-400 focus:border-sky-400"
      />
      <button class="w-full bg-sky-500 text-white py-2 rounded mt-4 hover:bg-sky-700">Registrarse</button>
      <p v-if="message" class="mt-2 text-green-700">{{ message }}</p>
    </form>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import { useContestantStore } from '@/stores/contestantStore'

export default {
  setup() {
    const name = ref('')
    const email = ref('')
    const phone = ref('')
    const message = ref('')
    const store = useContestantStore()

    const register = async () => {
      try {
        await store.register({
          name: name.value,
          email: email.value,
          phone: phone.value
        });
        message.value = '¡Gracias por registrarte! Revisa tu correo para verificar tu cuenta.';
      } catch (err) {
        message.value = store.error || 'Ocurrió un error al registrarte';
      }
    };

    return { name, email, phone, message, register }
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