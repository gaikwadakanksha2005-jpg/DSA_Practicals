
class Node:
    def __init__(self, patient_id, name, priority):
        self.patient_id = patient_id
        self.name = name
        self.priority = priority
        self.next = None

# Hospital class
class Hospital:
    def __init__(self):
        self.head = None

    # 1. Add Patient (Enqueue)
    def enqueue(self, patient_id, name, priority):
        new_node = Node(patient_id, name, priority)

        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if self.head is None:
            print("No patients waiting.")
        else:
            print("Next Patient:")
            print("Patient ID:", self.head.patient_id)
            print("Patient Name:", self.head.name)
            print("Priority:", self.head.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):
        if self.head is None:
            print("No patients to remove.")
        else:
            temp = self.head
            print("Treated Patient:", temp.name)
            self.head = self.head.next

    # 4. Display All Patients
    def display_all(self):
        if self.head is None:
            print("No waiting patients.")
        else:
            temp = self.head
            print("\nWaiting Patients:")
            while temp is not None:
                if temp.priority == 1:
                    status = "Critical"
                elif temp.priority == 2:
                    status = "Serious"
                else:
                    status = "Normal"
                print("ID:", temp.patient_id,
                      "Name:", temp.name,
                      "Priority:", status)
                temp = temp.next

h = Hospital()
while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority >= 1 and priority <= 3:
            h.enqueue(pid, name, priority)
        else:
            print("Invalid Priority!")
    elif choice == 2:
        h.display_next()
    elif choice == 3:
        h.dequeue()
    elif choice == 4:
        h.display_all()
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
