<template>
  <div class="p-2 m-auto text-center">
    <div class="flex items-center justify-center p-2">
      <img class="h-20 mx-2.5" src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png" alt="Flask logo">
      <img class="h-20 mx-2.5" src="https://vuejs.org/images/logo.png" alt="Vue logo">
      <img class="h-20 mx-2.5" src="https://avatars.githubusercontent.com/u/47703742?s=200&v=4" alt="Inertia logo">
      <img class="h-20 mx-2.5" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" alt="Inertia logo">
      <img class="h-20 mx-2.5" src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Vitejs-logo.svg" alt="Inertia logo">
    </div>
    {% raw %}
    <h1 class="p-2 text-3xl font-bold">Welcome to your Flask-Inertia {{ frameworkName }} app.</h1>
    {% endraw %}
    <p class="p-2 text-stone-500">
      For more information please visit the
      <a class="text-blue-600 underline hover:text-blue-800 visited:text-purple-600" href="https://flask-inertia.readthedocs.io/">documentation</a>.
    </p>

    <p class="p-2 text-stone-500">
      Sample route
      <Link class="text-blue-600 underline hover:text-blue-800 visited:text-purple-600" :href="$route('main.about')">url</Link>.
    </p>
  </div>
</template>

<script setup>
import { Link } from '@inertiajs/vue3'
const frameworkName = 'Vue'
</script>
