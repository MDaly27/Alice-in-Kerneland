(function(){
  const jokes = [
    "Why did the White Rabbit miss the deploy? Too many late commits.",
    "Off with their headers! — said the Queen after a 400 Bad Request.",
    "We're all mad here — especially the thread scheduler.",
    "Cheshire Catbranch: appears in git log, disappears on fetch.",
    "Caterpillar: ‘Who are you?’ — uname -a, obviously.",
    "Alice fell into an event loop and couldn't callback out.",
    "Mad Hatter writes tests first: T(ea)DD.",
    "The March Hare always runs with --force-with-lease — cautiously reckless.",
    "Down the rabbit hole? Check your call stack depth.",
    "Queen of Hearts: Off with their HEAD! (but make a backup tag)",
    "Cheshire smile: undefined behavior that still passes CI.",
    "Wonderland security: TLS (Tea Leaves Security).",
    "The Dormouse keeps everything in cache — he never forgets to sleep.",
    "Why is a raven like write-only memory? Both store but never return.",
    "Tweedle-Dee and Tweedle-Dum: two microservices with circular dependencies.",
  ];

  function pick() { return jokes[Math.floor(Math.random() * jokes.length)]; }

  function setJoke() {
    const el = document.getElementById('joke');
    if (el) el.textContent = pick();
  }

  window.addEventListener('DOMContentLoaded', () => {
    setJoke();
    const btn = document.getElementById('jokeButton');
    if (btn) btn.addEventListener('click', setJoke);
  });
})();