# Βήμα 1: Παίρνουμε τις εισόδους από τον χρήστη και τις αποθηκεύουμε σε μεταβλητές.
user_name = str(input("What is your name? "))
user_sirname = str(input("What is your sirname?"))

# Βήμα 2: Ορίζουμε τη συνάρτηση.
# Η συνάρτηση παίρνει δύο παραμέτρους (το όνομα και το επώνυμο).
def full_name(name, sirname):
    # Εδώ χρησιμοποιούμε τις παραμέτρους για να εκτυπώσουμε το μήνυμα.
    print(f"Nice to meet you {name} {sirname}")

# Βήμα 3: Καλούμε τη συνάρτηση.
# Περνάμε τις μεταβλητές που δημιουργήσαμε ως παραμέτρους.
full_name(user_name, user_sirname)