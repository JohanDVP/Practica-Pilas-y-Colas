class Node:

    __slots__ = ("__value", "__next")

    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise TypeError("El nodo no puede contener valores nulos")
        self.__value = new_value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, Node):
            raise TypeError("El next de un nodo, solo puede ser None ó un objeto tipo nodo")
        self.__next = new_next


class slinkedlist:

    __slots__ = ("__head", "__tail", "__size")

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self, new_head):
        if new_head is not None and not isinstance(new_head, Node):
            raise TypeError("La cabeza de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
        self.__head = new_head

    @tail.setter
    def tail(self, new_tail):
        if new_tail is not None and not isinstance(new_tail, Node):
            raise TypeError("La cola de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
        self.__tail = new_tail

    @size.setter
    def size(self, new_size):
        if new_size < 0 and not isinstance(new_size, int):
            raise TypeError("El tamaño de una lista enlazada, solo puede ser un numero entero mayor ó igual a cero")
        self.__size = new_size

    def __iter__(self):
        cur_node = self.__head

        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __str__(self):
        result = [str(temp_node.value) for temp_node in self]
        return ' --> '.join(result)

    def prepend(self, new_value):
        new_node = Node(new_value)

        new_node.next = self.__head
        if self.__head is None:
            self.__tail = new_node
        self.__head = new_node

        self.__size += 1

    def append(self, new_value):
        new_node = Node(new_value)

        if self.__head is None:
            self.__head = new_node
        else:
            self.__tail.next = new_node

        self.__tail = new_node
        self.__size += 1

    def getbyIndex(self, index):

        if not isinstance(index, int) or index > self.__size - 1 or index < -1:
            raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

        if index == 0:
            return self.head.value
        elif index == -1 or index == self.__size - 1:
            return self.__tail.value
        else:
            index_temp = 0

            for cur_node in self:
                if index_temp == index:
                    return cur_node.value
                index_temp += 1

    def getNodebyIndex(self, index):

        if not isinstance(index, int) or index > self.__size - 1 or index < -1:
            raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

        if index == 0:
            return self.head
        elif index == -1 or index == self.__size - 1:
            return self.__tail
        else:
            index_temp = 0

            for cur_node in self:
                if index_temp == index:
                    return cur_node
                index_temp += 1

    def InsertbyIndex(self, index, new_value):

        if not isinstance(index, int) or index > self.__size or index < -1:
            raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

        if index == 0:
            self.prepend(new_value)
        elif index == -1 or index == self.__size:
            self.append(new_value)
        else:
            new_node = Node(new_value)
            prev_node = self.getNodebyIndex(index - 1)
            print("prev_node", prev_node)
            print("new_node", new_node)

            new_node.next = prev_node.next
            prev_node.next = new_node
            self.__size += 1

    def searchvalue(self, value_to_find):
        for cur_node in self:
            if value_to_find == cur_node.value:
                return True

        return False

    def set_newvalue(self, value, new_value):
        for cur_node in self:
            if value == cur_node.value:
                cur_node.value = new_value

        return False

    def popfirst(self):
        if self.__head is None:
            raise TypeError("No hay elementos para retornar")
        elif self.__head is self.__tail:
            temp_value = self.__head.value
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            temp_value = self.__head.value
            self.__head = self.__head.next
            self.__size -= 1

        return temp_value

    def pop(self):
        if self.__head is None:
            raise TypeError("No hay elementos para retornar")
        elif self.__head is self.__tail:
            temp_value = self.__head.value
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            temp_value = self.__tail.value

            for cur_node in self:
                if cur_node.next is self.__tail:
                    prev_tail = cur_node

            prev_tail.next = None
            self.__tail = prev_tail
            self.__size -= 1

        return temp_value


class Queue:

    def __init__(self):
        self.__q = slinkedlist()

    def __str__(self):
        result = [str(nodo.value) for nodo in self.__q]
        return '--'.join(result)

    def enqueue(self, e):
        self.__q.append(e)
        return True

    def dequeue(self):
        if not self.is_empty():
            return self.__q.popfirst()
        else:
            raise TypeError("La cola esta vacia, no hay elementos para desencolar")

    def first(self):
        if not self.is_empty():
            # return self.__q.getbyIndex(0)
            return self.__q.head.value
        else:
            raise TypeError("La cola esta vacia, no hay elementos para leer")

    def is_empty(self):
        return self.__q.size == 0

    def len(self):
        return self.__q.size


class Stack:

    def __init__(self):
        self.__s = slinkedlist()

    def __str__(self):
        result = [str(nodo.value) for nodo in self.__s]
        return '||'.join(result)

    def push(self, e):
        self.__s.append(e)
        return True

    def pop(self):
        if not self.is_empty():
            return self.__s.pop()
        else:
            raise TypeError("La pila esta vacia, no hay elementos para desapilar")

    def top(self):
        if not self.is_empty():
            # return self.__q.getbyIndex(0)
            return self.__s.tail.value
        else:
            raise TypeError("La pila esta vacia, no hay elementos para leer")

    def is_empty(self):
        return self.__s.size == 0

    def len(self):
        return self.__s.size

class Solicitud:
    def __init__(self, id, descripcion, tipo):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo

    def __str__(self):
        return f"[{self.id}]" 

class Area:
    def __init__(self, nombre, capacidad, prioridad = False):
            self.nombre = nombre
            self.capacidad = capacidad

            if prioridad:
                self.cola_alta_prioridad = Queue()
                self.cola_normal_prioridad = Queue()
            else:
                self.espera = Queue()

            self.cola_nuevas = Queue()

Recepcion = Area("Recepcion y Triaje", 4, True)
Diagnostico = Area("Diagnostico Tecnico", 2)
Reparacion = Area("Reparacion / Correccion", 2)
Control = Area("Control de Calidad y Cierre", 1)

pila_areas = Stack()
pila_areas.push(Control)       
pila_areas.push(Reparacion)
pila_areas.push(Diagnostico)
pila_areas.push(Recepcion)

contador_IDs = 1
def ejecutar_turno():

    pila_aux = Stack()

    while not pila_areas.is_empty():

        area = pila_areas.pop()
        procesadas = 0

        if area.nombre == "Recepcion y Triaje":

            while procesadas < area.capacidad:

                if not area.cola_alta_prioridad.is_empty():
                    solicitud = area.cola_alta_prioridad.dequeue()

                elif not area.cola_normal_prioridad.is_empty():
                    solicitud = area.cola_normal_prioridad.dequeue()

                else:
                    break

                area.cola_nuevas.enqueue(solicitud)
                procesadas += 1

        else:

            capacidad = area.capacidad

            if area.espera.len() > 5:
                capacidad = capacidad // 2

                if capacidad < 1:
                    capacidad = 1

                print(f"Alerta: {area.nombre} esta sobrecargada")

            while procesadas < capacidad and not area.espera.is_empty():

                solicitud = area.espera.dequeue()
                area.cola_nuevas.enqueue(solicitud)
                procesadas += 1

        if not pila_areas.is_empty():

            siguiente = pila_areas.top()

            while not area.cola_nuevas.is_empty():
                siguiente.espera.enqueue(area.cola_nuevas.dequeue())

        else:

            while not area.cola_nuevas.is_empty():
                area.cola_nuevas.dequeue()

        print(f"{area.nombre}: {procesadas} procesadas")

        pila_aux.push(area)

    while not pila_aux.is_empty():
        pila_areas.push(pila_aux.pop())

while True:
    print("\n=== Bienvenido Usuario ===\n")

    print("1. Registrar Solicitud: ")
    print("2. Ejecutar un Turno Manual: ")
    print("3. Ejecutar Automaticamente: ")
    print("4. Eliminar un Area: ")
    print("5. Agregar Nueva Area: ")
    print("6. Consultar Estado del Sistema: ")
    print("7. Cierre")

    opcion = input("\nSeleccione una opcion para continuar: \n")

    if opcion == "1":
        id_solicitud = f"S{contador_IDs}"
        descripcion = input("Ingrese la descripcion del problema: ")
        tipo = input("Ingrese el tipo de prioridad (Alta / Normal)").strip().capitalize()

        if tipo not in ["Alta", "Normal"]:
            print("Error: El tipo de solicitud solo puede ser Alta o Normal")
            continue

        contador_IDs += 1

        nueva_solicitud = Solicitud(id_solicitud, descripcion, tipo)

        area_tope = pila_areas.top()

        if tipo == "Alta":
            area_tope.cola_alta_prioridad.enqueue(nueva_solicitud)
        else:
            area_tope.cola_normal_prioridad.enqueue(nueva_solicitud)

        print(f"Solicitud {id_solicitud} creada exitosamente")

    elif opcion == "2":
        print("\n========== TURNO MANUAL ==========")

        ejecutar_turno()

    elif opcion == "3":

        turno = 1

        while True:

            hay_solicitudes = False

            pila_aux = Stack()

            while not pila_areas.is_empty():

                area = pila_areas.pop()

                if area.nombre == "Recepcion y Triaje":
                    if not area.cola_alta_prioridad.is_empty() or not area.cola_normal_prioridad.is_empty():
                        hay_solicitudes = True
                else:
                    if not area.espera.is_empty():
                        hay_solicitudes = True

                pila_aux.push(area)

            while not pila_aux.is_empty():
                pila_areas.push(pila_aux.pop())

            if not hay_solicitudes:
                break

            print(f"\n========== TURNO {turno} ==========")

            ejecutar_turno()

            turno += 1

        print("\nTodas las solicitudes fueron procesadas.")

    elif opcion == "4":
        nombre_eliminar = input("Ingresa el nombre del area que quieras eliminar").strip().lower()

        pila_aux = Stack()
        area_buscada = None

        while not pila_areas.is_empty():
            current_area = pila_areas.pop()
            if current_area.nombre.lower() == nombre_eliminar:
                area_buscada = current_area
                break
            else:
                pila_aux.push(current_area)

        if area_buscada is None:
            print(f"No se encontró el Area {nombre_eliminar}")

            while not pila_aux.is_empty():
                pila_areas.push(pila_aux.pop())
        else:
            while not pila_aux.is_empty():
                pila_areas.push(pila_aux.pop())

            tope = pila_areas.top()

            if area_buscada.nombre == "Recepcion y Triaje":
                while not area_buscada.cola_alta_prioridad.is_empty():
                    solicitudes = area_buscada.cola_alta_prioridad.dequeue()
                    tope.espera.enqueue(solicitudes)
                while not area_buscada.cola_normal_prioridad.is_empty():
                    solicitudes = area_buscada.cola_normal_prioridad.dequeue()
                    tope.espera.enqueue(solicitudes)

            else:
                while not area_buscada.espera.is_empty():
                    solicitudes = area_buscada.espera.dequeue()
                    if tope.nombre == "Recepcion y Triaje":
                        tope.cola_normal_prioridad.enqueue(solicitudes)
                    else:
                        tope.espera.enqueue(solicitudes)

            print(f"Area {area_buscada.nombre} eliminada correctamente, y sus solicitudes fueron reubicadas en {tope.nombre} ")


    elif opcion == "5":
        nombre_area = input("Ingrese el nombre de la nueva area: ")

        capacidad_area = int(input("Ingrese la capacidad del area (numerica): "))

        if capacidad_area <= 0:
            print("Error: La capacidad debe ser mayor a 0")
        else:
            nueva_area = Area(nombre_area, capacidad_area)

            pila_areas.push(nueva_area)
            print(f"Area {nombre_area} creada y agregada correctamente")


    elif opcion == "6":

        pila_aux = Stack()
        posicion = 1

        while not pila_areas.is_empty():
            current_area = pila_areas.pop()

            if current_area.nombre == "Recepcion y Triaje":
                pendientes = current_area.cola_alta_prioridad.len() + current_area.cola_normal_prioridad.len()
                sobrecargada = "Recepcion y Triaje no tiene limite"  
            else:
                pendientes = current_area.espera.len()
                if pendientes > 5:
                    sobrecargada = "Si"  
                else: 
                    sobrecargada = "No" 

            print(f"{posicion}. Area: {current_area.nombre} (Capacidad: {current_area.capacidad}) | [SOBRECARGADA: {sobrecargada}]")

            if current_area.nombre == "Recepcion y Triaje":
                print(f"Cola Alta Prioridad : {current_area.cola_alta_prioridad}")
                print(f"Cola Normal Prioridad: {current_area.cola_normal_prioridad}")
            else:
                print(f"Cola de espera: {current_area.espera}")

            pila_aux.push(current_area)
            posicion += 1

        while not pila_aux.is_empty():
            pila_areas.push(pila_aux.pop()) 





        





