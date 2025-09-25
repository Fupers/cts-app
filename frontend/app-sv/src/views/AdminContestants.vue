<template>
  <div class="min-h-screen bg-sky-50">
    <AdminNavbar />

    <div class="p-8">
      <h1 class="text-2xl font-bold mb-4 text-sky-700">Lista de Concursantes</h1>

      <input
        v-model="search"
        placeholder="Buscar..."
        class="input mb-4 bg-sky-50"
      />

      <table class="w-full border">
        <thead>
          <tr class="bg-gray-200">
            <th class="p-2 border">Nombre</th>
            <th class="p-2 border">Correo</th>
            <th class="p-2 border">Verificado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="c in filteredContestants" :key="c.id" class="border">
            <td class="p-2 border">{{ c.name }}</td>
            <td class="p-2 border">{{ c.email }}</td>
            <td class="p-2 border">{{ c.is_verified ? 'Sí' : 'No' }}</td>
          </tr>
        </tbody>
      </table>

      <div class="flex justify-between items-center mt-4">
        <button
          @click="prevPage"
          :disabled="!store.previous"
          class="px-4 py-2 bg-gray-300 rounded disabled:opacity-50"
        >
          Anterior
        </button>

        <span>Página {{ currentPage }} de {{ totalPages }}</span>

        <button
          @click="nextPage"
          :disabled="!store.next"
          class="px-4 py-2 bg-gray-300 rounded disabled:opacity-50"
        >
          Siguiente
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, computed, onMounted } from "vue";
import { useContestantStore } from "../stores/contestantStore";
import AdminNavbar from "../components/AdminNavbar.vue";

export default {
  components: { AdminNavbar },
  setup() {
    const store = useContestantStore();
    const search = ref("");
    const currentPage = ref(1);

    const filteredContestants = computed(() => {
      return store.contestants.filter(
        (c) =>
          c.name.toLowerCase().includes(search.value.toLowerCase()) ||
          c.email.toLowerCase().includes(search.value.toLowerCase())
      );
    });

    const totalPages = computed(() => Math.ceil(store.total / 20));

    const fetchPage = (page: number) => {
      store.fetchContestants(page);
      currentPage.value = page;
    };

    const nextPage = () => {
      if (store.next) fetchPage(currentPage.value + 1);
    };

    const prevPage = () => {
      if (store.previous && currentPage.value > 1) fetchPage(currentPage.value - 1);
    };

    onMounted(() => fetchPage(currentPage.value));

    return { store, search, filteredContestants, currentPage, totalPages, nextPage, prevPage };
  },
};
</script>

<style scoped>
.input {
  display: block;
  width: 250px;
  height: 30px;
  padding: 0.5rem;
  margin-bottom: 0.75rem;
  border: 1px solid #adadadff;
  border-radius: 0.375rem;
}
</style>

