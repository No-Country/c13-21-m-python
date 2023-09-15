function fetcherFunction(url) {
    return fetch(url).then(response => response.json());
}
   
export default fetcherFunction;