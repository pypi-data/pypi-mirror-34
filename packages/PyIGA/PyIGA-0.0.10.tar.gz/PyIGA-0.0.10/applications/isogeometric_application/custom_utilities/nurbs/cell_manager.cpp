#include "custom_utilities/nurbs/cell_manager.h"

namespace Kratos
{

bool CellManager_RtreeSearchCallback(std::size_t id, void* arg)
{
    typedef std::vector<std::size_t> data_t;
    data_t* p_hits = (data_t*)(arg);
    p_hits->push_back(id);
    return true; // keep going
}

}

