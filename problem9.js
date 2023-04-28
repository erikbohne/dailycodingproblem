function jobScheduler(f, n) {
  setTimeout(f, n);
}

// Example usage:
jobScheduler(() => {
  console.log('hello, world!');
}, 1000);