function autocomplete(set, string) {
    const new_set = [];
    for (let i = 0; i < set.length; i++) {
      if (set[i].substring(0, string.length) === string) {
        new_set.push(set[i]);
      }
    }
    return new_set;
  }
  
  // Example usage:
  let set = ["dog", "deer", "deal"];
  let string = "de";
  console.log(autocomplete(set, string));