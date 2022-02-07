class Object:

    def update_pos(self, screen):
        screen.blit(self.surf, (self.x_pos,self.y_pos))