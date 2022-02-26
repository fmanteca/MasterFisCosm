{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Proceso de optimización de la red\n",
    "\n",
    "Enumera en la siguiente celda de Markdown las distintas arquitecturas que se han entrenado, incluyendo la motivación y resultados/mejoras de los distintos entrenamientos."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.(EJEMPLO)\n",
    "\n",
    "* Architectura: Hidden layers: 10, Optimizer: Adam, learning rate: 0.001, batch size: 512, epochs: 200.\n",
    "* Motivación: Reducción del learning rate para intentar acercanos más al mínimo de la función de pérdida.\n",
    "* Resultados: mejora en val_loss de 0.70 a 0.75\n",
    "\n",
    "2.\n",
    "\n",
    "\n",
    "3.\n",
    "\n",
    "\n",
    "...."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arquitectura Propuesta 1\n",
    "\n",
    "Copia en la siguiente celda el modelo final utilizado para obtener el fichero result.npy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (EJEMPLO)\n",
    "\n",
    "model = keras.models.Sequential()\n",
    "model.add(keras.layers.Flatten(input_shape=(40,40,1)))\n",
    "model.add(keras.layers.Dense(2, activation='softmax'))\n",
    "\n",
    "model.compile(loss='categorical_crossentropy', optimizer=\"adam\", metrics = [\"accuracy\"])\n",
    "\n",
    "model.fit(images_train, keras.utils.to_categorical(df_train[\"is_signal_new\"]), epochs=5, validation_data=(images_val,keras.utils.to_categorical(df_val[\"is_signal_new\"])))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arquitectura Propuesta 2\n",
    "\n",
    "Copia en la siguiente celda el modelo final utilizado para obtener el fichero result.npy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (EJEMPLO)\n",
    "\n",
    "model = keras.models.Sequential()\n",
    "model.add(keras.layers.Flatten(input_shape=(40,40,1)))\n",
    "model.add(keras.layers.Dense(2, activation='softmax'))\n",
    "\n",
    "model.compile(loss='categorical_crossentropy', optimizer=\"adam\", metrics = [\"accuracy\"])\n",
    "\n",
    "model.fit(images_train, keras.utils.to_categorical(df_train[\"is_signal_new\"]), epochs=20, validation_data=(images_val,keras.utils.to_categorical(df_val[\"is_signal_new\"])))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
