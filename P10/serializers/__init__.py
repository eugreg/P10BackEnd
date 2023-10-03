from .produto import  ProdutosDetailSerializer, ProdutosListSerializer, ProdutosSerializer, ProdutosCreateSerializer
from .fornecedor import FornecedorDetailSerializer, FornecedorListSerializer, FornecedorSerializer
from .categoria import  CategoriaSerializer
from .descontos import DescontoSerializer
from .subcategoria import SubCategoriaSerializer
from .sazonal import SazonalSerializer
from .marca import MarcaSerializer
from .compra import CompraSerializer,ItensCompraSerializer, CriarEditarCompraSerializer, CriarEditarItenSerializer
from .tag import TagSerializer