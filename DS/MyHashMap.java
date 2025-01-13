public class MyHashMap<K, V>{

    private class Entry<K, V>{
        private K key;
        private V value;
        private Entry<K, V> next;

        public Entry(K key, V value){
            this.key = key;
            this.value = value;
        }

        public K getKey(){
            return key;
        }

        public V getValue(){
            return value;
        }

        public void setValue(V value){
            this.value = value;
        }

        @Override
        public String toString() {
            Entry<K, V> temp = this;
            StringBuilder builder = new StringBuilder();
            while (temp != null){
                builder.append(temp.key + " -> " + temp.value + ",");
                temp = temp.next;
            }
            return builder.toString();
        }
    }

    private final int SIZE = 5;
    //If your size is too large you may not have collisions (values with the same hashcode)
    // but for this example I am making it small enough to have collisions

    private Entry<K, V>[] table;

    public MyHashMap(){
        table = new Entry[SIZE];
    }

    public void put(K key, V value) {
        int hash = key.hashCode() % SIZE;
        Entry<K, V> entry = table[hash];

        if (entry == null){
            table[hash] = new Entry<>(key, value);
        } else {
            while (entry.next != null) {
                if (entry.getKey() == key) {
                    entry.setValue(value);
                    return;
                } else {
                    entry = entry.next;
                }
            }

            if (entry.getKey() == key) {
                entry.setValue(value);
            } else {
                entry.next = new Entry<>(key, value);
            }
        }
    }

    public V get(K key) {
        int hash = key.hashCode() % SIZE;
        Entry<K, V> entry = table[hash];

        if (entry == null){
            return null;
        }

        while (entry.next != null) {
            if (entry.getKey() == key) {
                return entry.getValue();
            }
            entry = entry.next;
        }

        return null;
    }

    public Entry<K, V> remove(K key) {
        int hash = key.hashCode() % SIZE;
        Entry<K, V> entry = table[hash];

        if (entry == null){
            return null;
        }

        if (entry.getKey() == key) {
            table[hash] = entry.next;
            entry.next = null;
            return entry;
        }

        Entry<K, V> prev = entry;
        entry = entry.next;

        while (entry != null) {
            if (entry.getKey() == key) {
                prev.next = entry.next;
                entry.next = null;
                return entry;
            }
            prev = entry;
            entry = entry.next;
        }

        return null;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < SIZE; i++) {
            if (table[i] != null) {
                sb.append(i + " " + table[i] + "\n");
            } else {
                sb.append(i + " " + "null" + "\n");
            }
        }

        return sb.toString();
    }
}
